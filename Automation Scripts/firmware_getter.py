import requests
from lxml.html import fromstring as etree_fromstring
from pathlib import PosixPath
import shutil

URL = "https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/amdgpu"
NEEDED_FIRMWARE = [
	"navi12_gpu_info.bin",
	"arcturus_gpu_info.bin",
	"arcturus_ta.bin",
	"arcturus_asd.bin",
	"arcturus_sos.bin",
	"navi12_ta.bin",
	"navi12_asd.bin",
	"navi12_sos.bin",
	"arcturus_rlc.bin",
	"arcturus_mec2.bin",
	"arcturus_mec.bin",
	"navi12_rlc.bin",
	"navi12_mec2.bin",
	"navi12_mec.bin",
	"navi12_me.bin",
	"navi12_pfp.bin",
	"navi12_ce.bin",
	"arcturus_sdma.bin",
	"navi12_sdma1.bin",
	"navi12_sdma.bin",
	"navi10_mes.bin",
	"navi12_vcn.bin",
	"arcturus_vcn.bin",
	"navi12_smc.bin",
	"arcturus_smc.bin",
	"navi12_dmcu.bin"
]
LOCATION = PosixPath("/lib/firmware/amdgpu")


def download_file(link, file_name):
    # Now that we have both the firmware file name and the link to download the '.bin' file, download and write them
    bin_file = requests.get(link)
    with open(file_name, "wb") as fout:
        fout.write(bin_file.content)
        fout.flush()


def process_file(link):
    # Use the text of the link to create the filename, fetch the url and get the link to download the file
    firmware = LOCATION.joinpath(link.text)
    url = link.get("href")
    print(f"{firmware} => {url}")
    bin_file = requests.get(url)
    etree = etree_fromstring(bin_file.text)
    etree.make_links_absolute(URL)
    download_file(etree.xpath("//div[@class='content']/a/@href")[0], firmware)


if __name__ == "__main__":
    # First fetch the URL and get all the links to firmware files
    response = requests.get(URL)
    etree = etree_fromstring(response.text)
    etree.make_links_absolute(URL)  # Needed since all the links in the document is relative
    for element in etree.xpath("//a[contains(@class, 'ls-blob')]"):
        # If the current firmware file is one that is needed then proceed to download it
        if element.text in NEEDED_FIRMWARE:
            process_file(element)

