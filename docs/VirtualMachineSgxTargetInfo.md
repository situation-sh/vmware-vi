# VirtualMachineSgxTargetInfo

Description of Intel Software Guard Extensions information.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_epc_size** | **int** | Maximum size, in bytes, of EPC available on the compute resource.  ***Since:*** vSphere API 7.0  | 
**flc_modes** | **List[str]** | FLC modes available in the compute resource.  The set of possible values are described in *VirtualMachineSgxInfoFlcModes_enum*.  ***Since:*** vSphere API 7.0  | [optional] 
**le_pub_key_hashes** | **List[str]** | Public key hashes of the provider launch enclaves available in the compute resource.  ***Since:*** vSphere API 7.0  | [optional] 
**require_attestation_supported** | **bool** | Whether the host/cluster supports requiring SGX remote attestation.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_sgx_target_info import VirtualMachineSgxTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSgxTargetInfo from a JSON string
virtual_machine_sgx_target_info_instance = VirtualMachineSgxTargetInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSgxTargetInfo.to_json()

# convert the object into a dict
virtual_machine_sgx_target_info_dict = virtual_machine_sgx_target_info_instance.to_dict()
# create an instance of VirtualMachineSgxTargetInfo from a dict
virtual_machine_sgx_target_info_form_dict = virtual_machine_sgx_target_info.from_dict(virtual_machine_sgx_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


