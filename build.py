from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="Gumbo:shared", pure_c=False) # pure_c=False needed for Visual Studio support
    builder.run()
