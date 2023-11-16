# HostSgxRegistrationInfo

Data object describing SGX host registration information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | SGX host registration status.  Valid values come from *HostSgxRegistrationInfoRegistrationStatus_enum* enum. Set, except in case of an internal error.  | [optional] 
**bios_error** | **int** | BIOS error related to SGX host registration.  Set only if SGX registration status is incomplete.  | [optional] 
**registration_url** | **str** | SGX host registration URL.  Unset if SGX registration status is not applicable or in case of an internal error.  | [optional] 
**type** | **str** | SGX host registration type.  Valid values come from *HostSgxRegistrationInfoRegistrationType_enum* enum. Unset if SGX registration status is not applicable, complete, or in case of an internal error.  | [optional] 
**ppid** | **str** | Platform Provisioning ID (PPID).  Hex-encoded representation of the the PPID (Platform Provisioning ID), returned as the response to a successful registration request. This field is populated only on the vCenter through which the host has been registered.  | [optional] 
**last_registered_time** | **datetime** | Timestamp of last successful registration from this vCenter.  | [optional] 

## Example

```python
from vmware_vi.models.host_sgx_registration_info import HostSgxRegistrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSgxRegistrationInfo from a JSON string
host_sgx_registration_info_instance = HostSgxRegistrationInfo.from_json(json)
# print the JSON string representation of the object
print HostSgxRegistrationInfo.to_json()

# convert the object into a dict
host_sgx_registration_info_dict = host_sgx_registration_info_instance.to_dict()
# create an instance of HostSgxRegistrationInfo from a dict
host_sgx_registration_info_form_dict = host_sgx_registration_info.from_dict(host_sgx_registration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


