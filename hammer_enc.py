import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))