# HostSgxInfo

Data object describing the Software Guard Extension (SGX) configuration on the ESXi host.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sgx_state** | **str** | SGX state of the host.  The set of supported values are described in *HostSgxInfoSgxStates_enum*.  ***Since:*** vSphere API 7.0  | 
**total_epc_memory** | **int** | Size of physical EPC in bytes.  ***Since:*** vSphere API 7.0  | 
**flc_mode** | **str** | FLC mode of the host.  The set of supported values are described in *HostSgxInfoFlcModes_enum*.  ***Since:*** vSphere API 7.0  | 
**le_pub_key_hash** | **str** | Public key hash of the provider launch enclave.  This is the SHA256 digest of the SIGSTRUCT.MODULUS(MR\\_SIGNER) of the provider launch enclave. This attribute is set only if attribute flcMode is locked.  ***Since:*** vSphere API 7.0  | [optional] 
**registration_info** | [**HostSgxRegistrationInfo**](HostSgxRegistrationInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_sgx_info import HostSgxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSgxInfo from a JSON string
host_sgx_info_instance = HostSgxInfo.from_json(json)
# print the JSON string representation of the object
print HostSgxInfo.to_json()

# convert the object into a dict
host_sgx_info_dict = host_sgx_info_instance.to_dict()
# create an instance of HostSgxInfo from a dict
host_sgx_info_form_dict = host_sgx_info.from_dict(host_sgx_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


