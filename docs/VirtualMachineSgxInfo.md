# VirtualMachineSgxInfo

This data object describes the virtual software guard extension (vSGX) configuration of this virtual machine.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epc_size** | **int** | Size of vEPC, in megabytes.  ***Since:*** vSphere API 7.0  | 
**flc_mode** | **str** | FLC mode for the virtual machine.  The set of possible values are described in *VirtualMachineSgxInfoFlcModes_enum*. If no value is specified, then \&quot;unlocked\&quot; will be used.  ***Since:*** vSphere API 7.0  | [optional] 
**le_pub_key_hash** | **str** | Public key hash of the provider launch enclave.  This is the SHA256 digest of the SIGSTRUCT.MODULUS(MR\\_SIGNER) of the provider launch enclave. This hash must only be provided when the launch enclave mode is \&quot;locked\&quot;, for the other cases the hash is ignored.  ***Since:*** vSphere API 7.0  | [optional] 
**require_attestation** | **bool** | Indicates whether or not a virtual machine requires remote attestation.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_sgx_info import VirtualMachineSgxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSgxInfo from a JSON string
virtual_machine_sgx_info_instance = VirtualMachineSgxInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSgxInfo.to_json()

# convert the object into a dict
virtual_machine_sgx_info_dict = virtual_machine_sgx_info_instance.to_dict()
# create an instance of VirtualMachineSgxInfo from a dict
virtual_machine_sgx_info_form_dict = virtual_machine_sgx_info.from_dict(virtual_machine_sgx_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


