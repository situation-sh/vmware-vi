# ArrayOfVsanHostFaultDomainInfo

A boxed array of *VsanHostFaultDomainInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostFaultDomainInfo]**](VsanHostFaultDomainInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_fault_domain_info import ArrayOfVsanHostFaultDomainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostFaultDomainInfo from a JSON string
array_of_vsan_host_fault_domain_info_instance = ArrayOfVsanHostFaultDomainInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostFaultDomainInfo.to_json()

# convert the object into a dict
array_of_vsan_host_fault_domain_info_dict = array_of_vsan_host_fault_domain_info_instance.to_dict()
# create an instance of ArrayOfVsanHostFaultDomainInfo from a dict
array_of_vsan_host_fault_domain_info_form_dict = array_of_vsan_host_fault_domain_info.from_dict(array_of_vsan_host_fault_domain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


