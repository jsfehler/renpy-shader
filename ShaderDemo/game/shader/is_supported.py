import renpy


class config:
    enabled = True
    fps = 60
    flipMeshX = True


def log(message):
    renpy.display.log.write("Shaders: " + message)


def isSupported(verbose=False):
    if not config.enabled:
        if verbose:
            log("Disabled because of 'config.enabled'")
        return False

    if not renpy.config.gl_enable:
        if verbose:
            log("Disabled because of 'renpy.config.gl_enable'")
        return False

    # TODO renpy.get_renderer_info()
    renderer = renpy.display.draw.info.get("renderer")
    if renderer != "gl":
        if verbose:
            log("Disabled because the renderer is '%s'" % renderer)
        return False

    if verbose:
        log("Supported!")

    return True
