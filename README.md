# AMACON
## Integration of AMA4000 in THN Test Environment

This repository will contain different approaches to integtrate an AMA4000 (Pierburg Systems) in an exsisting enginge test rigt at the Technische Hochschule Nürnberg.

The first stage of this project will be to create a generic (and simple) communication platform over the "AK-Protocol" using the serial (RS232) port to exchange data between a host (Master -> PC, Raspi, you name it ;) ) and AMA4000. AMA4000 will serve as a slave respondig to the given commands.

Furthermore the connected Master device will serve as a bridgehead to the AMA4000 network, allowing all devcies in the test rig environment to access and control AMA4000.
