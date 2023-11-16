# VirtualMachineToolsInstallTypeEnum

The installation type of tools in the VM.  Possible values: - `guestToolsTypeUnknown`: Installation type is not known.      Most likely tools have been   installed by OSPs or open-vm-tools, but a version that does   not report its install type or an install type that we do   not recognize. - `guestToolsTypeMSI`: MSI is the installation type used for VMware Tools on Windows. - `guestToolsTypeTar`: Tools have been installed by the tar installer. - `guestToolsTypeOSP`: OSPs are RPM or Debian packages tailored for the OS in the VM.      See http://packages.vmware.com - `guestToolsTypeOpenVMTools`: open-vm-tools are the open-source version of VMware Tools, may have   been packaged by the OS vendor.    ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


