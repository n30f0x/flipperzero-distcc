def exists():
    return True


def generate(env):
    if ccache := env.WhereIs("ccache"):
        if distcc := env.WhereIs("distcc"):
            env["CCACHE"] = "ccache"
            # env["CCACHE_PREFIX"] ="distcc"
            env["CC_NOCACHE"] = env["CC"]
            env["CC"] = "distcc $CCACHE $CC_NOCACHE"
            env["LINK"] = env["CXX"]
            env["CXX_NOCACHE"] = env["CXX"]
            env["CXX"] = "$CCACHE $CXX_NOCACHE"
        else:
            env["CCACHE"] = "ccache"
            env["CC_NOCACHE"] = env["CC"]
            env["CC"] = "$CCACHE $CC_NOCACHE"
            # Tricky place: linking is done with CXX
            # Using ccache breaks it
            env["LINK"] = env["CXX"]
            env["CXX_NOCACHE"] = env["CXX"]
            env["CXX"] = "$CCACHE $CXX_NOCACHE"