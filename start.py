from scrapy import cmdline


print("[Spider] running...")

cmdline.execute("scrapy crawl tencent".split())

print("[Spider] done")
