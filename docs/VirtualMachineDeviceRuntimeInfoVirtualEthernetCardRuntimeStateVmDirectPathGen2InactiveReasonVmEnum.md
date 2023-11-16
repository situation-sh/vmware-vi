# VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeStateVmDirectPathGen2InactiveReasonVmEnum

Possible values: - `vmNptIncompatibleGuest`: The virtual machine's guest OS does not support   VMDirectPath Gen 2. - `vmNptIncompatibleGuestDriver`: The virtual machine's guest network driver does not support   VMDirectPath Gen 2. - `vmNptIncompatibleAdapterType`: The device type does not support VMDirectPath Gen 2.      See also *VirtualEthernetCardOption.vmDirectPathGen2Supported*. - `vmNptDisabledOrDisconnectedAdapter`: The virtual machine's network adapter is disabled or   disconnected, and thus is not participating in VMDirectPath Gen 2. - `vmNptIncompatibleAdapterFeatures`: The virtual machine's network adapter has features enabled   which preclude it participating in VMDirectPath Gen 2 such   as INT-x or PXE booting. - `vmNptIncompatibleBackingType`: The device backing is not a DistributedVirtualPortBacking. - `vmNptInsufficientMemoryReservation`: The virtual machine does not have full memory reservation   required to activate VMDirectPath Gen 2. - `vmNptFaultToleranceOrRecordReplayConfigured`:       Deprecated as of vSphere API 6.0.      The virtual machine is configured for Fault Tolerance or   Record &amp; Replay, which prevents VMDirectPath Gen 2. - `vmNptConflictingIOChainConfigured`: Some networking feature has placed a conflicting IOChain on   the network adapter, which prevents VMDirectPath Gen 2.      Examples   include DVFilter. - `vmNptMonitorBlocks`: The virtual machine monitor is exercising functionality which   which prevents VMDirectPath Gen 2. - `vmNptConflictingOperationInProgress`: VMDirectPath Gen 2 is temporarily suspended while the virtual   machine executes an operation such as suspend. - `vmNptRuntimeError`: VMDirectPath Gen 2 is unavailable due to an unforeseen runtime error   in the virtualization platform (typically resource constraints.) - `vmNptOutOfIntrVector`: VMDirectPath Gen 2 is unavailable due to host run out of intr   vector in host.      Guest can configure the vNIC to use less rx/tx   queues or use MSI instead of MSIX. - `vmNptVMCIActive`: VMDirectPath Gen 2 is unavailable due to Incompatibe feature   VMCI is active in the current VM.      Kill the relevant VMCI   application(s) and restart the VM will allow the vNIC(s) to enter   passthrough mode.      ***Since:*** vSphere API 5.1  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

