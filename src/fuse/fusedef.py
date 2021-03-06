import sys, os

kMaxEfuseWords  = 80

##################################################

kEfuseIndex_START  = 0x0

kEfuseIndex_TESTER0  = 0x1
kEfuseIndex_TESTER1  = 0x2
kEfuseIndex_TESTER2  = 0x3
kEfuseIndex_TESTER3  = 0x4

kEfuseIndex_BOOT_CFG0  = 0x5
kEfuseIndex_BOOT_CFG1  = 0x6
kEfuseIndex_BOOT_CFG2  = 0x7

kEfuseIndex_OTPMK0 = 0x10
kEfuseIndex_OTPMK1 = 0x11
kEfuseIndex_OTPMK2 = 0x12
kEfuseIndex_OTPMK3 = 0x13
kEfuseIndex_OTPMK4 = 0x14
kEfuseIndex_OTPMK5 = 0x15
kEfuseIndex_OTPMK6 = 0x16
kEfuseIndex_OTPMK7 = 0x17

kEfuseIndex_SRK0 = 0x18
kEfuseIndex_SRK1 = 0x19
kEfuseIndex_SRK2 = 0x1A
kEfuseIndex_SRK3 = 0x1B
kEfuseIndex_SRK4 = 0x1C
kEfuseIndex_SRK5 = 0x1D
kEfuseIndex_SRK6 = 0x1E
kEfuseIndex_SRK7 = 0x1F

kEfuseIndex_SW_GP2_0 = 0x29
kEfuseIndex_SW_GP2_1 = 0x2A
kEfuseIndex_SW_GP2_2 = 0x2B
kEfuseIndex_SW_GP2_3 = 0x2C

kEfuseIndex_MISC_CONF0 = 0x2D
kEfuseIndex_MISC_CONF1 = 0x2E

kEfuseIndex_GP4_0 = 0x3C
kEfuseIndex_GP4_1 = 0x3D
kEfuseIndex_GP4_2 = 0x3E
kEfuseIndex_GP4_3 = 0x3F

##################################################

kEfuseMask_SecConfig0 = 0x00000002
kEfuseMask_SecConfig1 = 0x00000002
kEfuseShift_SecConfig0 = 1
kEfuseShift_SecConfig1 = 1
kEfuseLocation_SecConfig0 = kEfuseIndex_TESTER3
kEfuseLocation_SecConfig1 = kEfuseIndex_BOOT_CFG1

kEfuseMask_BtFuseSel = 0x00000010
kEfuseShift_BtFuseSel = 4
kEfuseLocation_BtFuseSel = kEfuseIndex_BOOT_CFG1

kEfuseMask_BeeKey0Sel = 0x00003000
kEfuseMask_BeeKey1Sel = 0x0000C000
kEfuseShift_BeeKey0Sel = 12
kEfuseShift_BeeKey1Sel = 14
kEfuseLocation_BeeKeySel = kEfuseIndex_BOOT_CFG1

kEfuseMask_EepromEnable   = 0x01000000
kEfuseShift_EepromEnable  = 24
kEfuseMask_LpspiIndex     = 0x06000000
kEfuseShift_LpspiIndex    = 25
kEfuseMask_SpiAddressing  = 0x08000000
kEfuseShift_SpiAddressing = 27
kEfuseMask_LpspiSpeed     = 0x30000000
kEfuseShift_LpspiSpeed    = 28
kEfuseLocation_LpspiCfg   = kEfuseIndex_MISC_CONF0

kEfuseMask_RawNandPortSize   = 0x00000008
kEfuseShift_RawNandPortSize  = 3
kEfuseMask_RawNandEccEdoSet  = 0x00000010
kEfuseShift_RawNandEccEdoSet = 4
kEfuseMask_RawNandEccStatus  = 0x01000000
kEfuseShift_RawNandEccStatus = 24
kEfuseLocation_SemcNandCfg   = kEfuseIndex_MISC_CONF1

##################################################

kHabStatus_FAB     = 0x0
kHabStatus_Open    = 0x1
kHabStatus_Closed0 = 0x2
kHabStatus_Closed1 = 0x3

kBeeKeySel_FromReg   = 0x0
kBeeKeySel_FromGp4   = 0x1
kBeeKeySel_FromOtpmk = 0x2
kBeeKeySel_FromSwGp2 = 0x3

kSpiAddressing_3Bytes = 0x0
kSpiAddressing_2Bytes = 0x1

##################################################
kEfuseRemapIndex_Src  = 0x30
kEfuseRemapIndex_Dest = 0x40
kEfuseRemapLen = 16

##################################################
kEfuseEntryModeRegion0IndexStart = 0x05
kEfuseEntryModeRegion0IndexEnd   = 0x07
kEfuseEntryModeRegion1IndexStart = 0x18
kEfuseEntryModeRegion1IndexEnd   = 0x1F
kEfuseEntryModeRegion2IndexStart = 0x29
kEfuseEntryModeRegion2IndexEnd   = 0x2E
kEfuseEntryModeRegion3IndexStart = 0x4C
kEfuseEntryModeRegion3IndexEnd   = 0x4F

