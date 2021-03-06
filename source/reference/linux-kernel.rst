.. _ref-linux-kernel:

Linux microPlatform Kernel
==========================

A common and unified Linux Kernel source tree is provided and used by
Linux microPlatform.

The latest continuous release is available to Linux microPlatform
subscribers at `source.foundries.io/linux.git`_.

.. todo:: add link to public kernel when available

The Linux Kernel recipe can be found in the :ref:`Meta-OSF layer
<ref-linux-layers-meta-osf>`, under the ``meta-osf/recipes-kernel/linux``
directory (linux-osf). You can find the common Linux distro config at
``meta-osf/recipes-kernel/linux/linux-osf/distro.cfg``, which
provides the base configs required by systemd, the Docker runtime, and
drivers for additional WiFi / Bluetooth adapters.

.. _source.foundries.io/linux.git: https://source.foundries.io/linux.git
