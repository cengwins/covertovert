docker exec -it receiver bash
cd /app/docs
cat > index.rst << 'EOL'
CENG 435 - Programming Assignment - Phase 1
=========================================

Group Information
---------------
Group ID: 23
Members:
- Pinar Aksoy (2374338)

Overview
--------------
Implementation of ICMP communication between containers:

* Sender: Creates ICMP packets with TTL=1
* Receiver: Captures and displays matching packets
* Successfully tested in Docker environment

Source Code Documentation
-----------------------

.. toctree::
   :maxdepth: 2

   modules
