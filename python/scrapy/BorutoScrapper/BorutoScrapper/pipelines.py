# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BorutoscrapperPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        # iterate over the local file paths of all downloaded images
        for result in [x for ok, x in results if ok]:
            path = result['path']
            # here we create the session-path where the files should be in the end
            # you'll have to change this path creation depending on your needs
            target_path = os.path.join(item['folder_path'], os.path.basename(path))

            if not os.path.isdir(target_path):
                os.makedirs(target_path)

            # try to move the file and raise exception if not possible
            if not os.rename(path, target_path):
                raise ImageException("Could not move image to target folder")

            # here we'll write out the result with the new path,
            # if there is a result field on the item (just like the original code does)
            if self.IMAGES_RESULT_FIELD in item.fields:
                result['path'] = target_path
                item[self.IMAGES_RESULT_FIELD].append(result)

        return item

