# VirtualMachineToolsVersionStatusEnum

Current version status of VMware Tools installed in the guest operating system.  Possible values: - `guestToolsNotInstalled`: VMware Tools has never been installed. - `guestToolsNeedUpgrade`:       Deprecated as of vSphere API 5.1 value is not reported by   toolsVersionStatus2, instead more detailed status is reported.      VMware Tools is installed, but the version is not current. - `guestToolsCurrent`: VMware Tools is installed, and the version is current. - `guestToolsUnmanaged`: VMware Tools is installed, but it is not managed by VMWare. - `guestToolsTooOld`: VMware Tools is installed, but the version is too old.      ***Since:*** vSphere API 5.0 - `guestToolsSupportedOld`: VMware Tools is installed, supported, but a newer version is available.      ***Since:*** vSphere API 5.0 - `guestToolsSupportedNew`: VMware Tools is installed, supported, and newer   than the version available on the host.      ***Since:*** vSphere API 5.0 - `guestToolsTooNew`: VMware Tools is installed, and the version is known to be   too new to work correctly with this virtual machine.      ***Since:*** vSphere API 5.0 - `guestToolsBlacklisted`: VMware Tools is installed, but the installed version is   known to have a grave bug and should be immediately upgraded.      ***Since:*** vSphere API 5.0  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


