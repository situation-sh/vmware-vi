# VmFaultToleranceConfigIssueReasonForIssueEnum

Possible values: - `haNotEnabled`: HA is not enabled on the cluster - `moreThanOneSecondary`: There is already a secondary virtual machine for the primary   virtual machine - `recordReplayNotSupported`:       Deprecated as of vSphere API 6.0.      The virtual machine does not support record/replay.      Vm::Capability.RecordReplaySupported is false. - `replayNotSupported`:       Deprecated as of vSphere API 6.0.      It is not possible to turn on Fault Tolerance on this powered-on VM.      The support for record/replay should be enabled or Fault Tolerance   turned on, when this VM is powered off. - `templateVm`: The virtual machine is a template - `multipleVCPU`: The virtual machine has more than one virtual CPU - `hostInactive`: The host is not active - `ftUnsupportedHardware`: The host ftSupported flag is not set because of hardware issues - `ftUnsupportedProduct`: The host ftSupported flag is not set because of it is a   VMware Server 2.0 - `missingVMotionNic`: No VMotion license or VMotion nic is not configured on the host - `missingFTLoggingNic`: FT logging nic is not configured on the host - `thinDisk`: The virtual machine has thin provisioned disks - `verifySSLCertificateFlagNotSet`: The \"check host certificate\" flag is not set - `hasSnapshots`: The virtual machine has one or more snapshots - `noConfig`: No configuration information is available for the virtual machine - `ftSecondaryVm`: The virtual machine is a fault tolerance secondary virtual machine - `hasLocalDisk`: The virtual machine has one or more disks on local datastore - `esxAgentVm`: The virtual machine is an ESX agent VM      ***Since:*** vSphere API 5.0 - `video3dEnabled`: The virtual machine video device has 3D enabled      ***Since:*** vSphere API 5.0 - `hasUnsupportedDisk`: ***Since:*** vSphere API 5.1 - `insufficientBandwidth`: FT logging nic does not have desired bandwidth      ***Since:*** vSphere API 6.0 - `hasNestedHVConfiguration`: The host does not support fault tolerant VM with nested HV or VBS   enabled.      ***Since:*** vSphere API 5.1 - `hasVFlashConfiguration`: The virtual machine has a vFlash memory device or/and disks with   vFlash cache configured.      ***Since:*** vSphere API 5.5 - `unsupportedProduct`: VMware product installed on the host does not support   fault tolerance      ***Since:*** vSphere API 6.0 - `cpuHvUnsupported`: Host CPU does not support hardware virtualization      ***Since:*** vSphere API 6.0 - `cpuHwmmuUnsupported`: Host CPU does not support hardware MMU virtualization      ***Since:*** vSphere API 6.0 - `cpuHvDisabled`: Host CPU is compatible for replay-based FT, but hardware   virtualization has been disabled in the BIOS.      ***Since:*** vSphere API 6.0 - `hasEFIFirmware`: The virtual machine firmware is of type EFI      ***Since:*** vSphere API 6.0 - `tooManyVCPUs`: The host does not support fault tolerance virtual machines   with the specified number of virtual CPUs.      ***Since:*** vSphere API 6.7 - `tooMuchMemory`: The host does not support fault tolerance virtual machines   with the specified amount of memory.      ***Since:*** vSphere API 6.7 - `vMotionNotLicensed`: No VMotion license      ***Since:*** vim FT_DRS_METRO_CLUSTER version - `ftNotLicensed`: Host does not have proper FT license      ***Since:*** vim FT_DRS_METRO_CLUSTER version - `haAgentIssue`: Host does not have HA agent running properly      ***Since:*** vim FT_DRS_METRO_CLUSTER version - `unsupportedSPBM`: The VM has unsupported storage policy      ***Since:*** vim FT_DRS_METRO_CLUSTER version - `hasLinkedCloneDisk`: The virtual machine has virtual disk in linked-clone mode      ***Since:*** vim FT_DRS_METRO_CLUSTER version - `unsupportedPMemHAFailOver`: Virtual Machine with Pmem HA Failover is not supported      ***Since:*** vSphere API 7.0.2.0 - `unsupportedEncryptedDisk`: Virtual Machine with encrypted virtual disk is not supported.      ***Since:*** vim FT_DRS_METRO_CLUSTER version - `ftMetroClusterNotEditable`: The virtual machine does not allow to enable or disable FT Metro   Cluster while FT is turned on.      ***Since:*** vim FT_DRS_METRO_CLUSTER version - `noVmRulesConfigured`: Cannot turn on vSphere Fault Tolerance on a FT Metro Cluster enabled VM   with no configured host affinity rules.      ***Since:*** vim FT_DRS_METRO_CLUSTER version  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

