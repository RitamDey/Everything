# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from .settings import IMAGES_STORE
import os
from shutil import move


class BorutoscrapperPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        # iterate over the local file paths of all downloaded images
        for result in [x for ok, x in results if ok]:
            path = os.path.join(IMAGES_STORE, result['path'])
            # here we create the session-path where the files should be in the end
            # you'll have to change this path creation depending on your needs
            target_path = os.path.join(IMAGES_STORE, item['folder_path'])

            if not os.path.isdir(target_path):
                os.makedirs(target_path)

            print(os.path.isdir(target_path), os.path.isdir(path))

            # try to move the file and raise exception if not possible
            if not move(path, target_path):
                raise ImageException("Could not move image to target folder")

            # here we'll write out the result with the new path,
            # if there is a result field on the item (just like the original code does)
            if self.IMAGES_RESULT_FIELD in item.fields:
                result['path'] = target_path
                item[self.IMAGES_RESULT_FIELD].append(result)

        return item
