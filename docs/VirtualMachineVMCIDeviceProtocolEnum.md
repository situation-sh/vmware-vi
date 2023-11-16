# VirtualMachineVMCIDeviceProtocolEnum

Set of possible values for protocol field in FilterSpec.  Possible values: - `hypervisor`: VMCI hypervisor datagram send op.      Direction code is not applicable to this one. - `doorbell`: VMCI doorbell notification - `queuepair`: VMCI queue pair alloc operation.      Direction code not applicable to this one. - `datagram`: VMCI and VMCI Socket datagram send op.      Since VMCI Socket datagrams map ports directly to resources,   there is no need to distinguish between the two. - `stream`: VMCI Stream Socket connect op. - `anyProtocol`: All of the above.    ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


