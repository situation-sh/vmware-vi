# EVCModeIllegalByVendor

An attempt to enable Enhanced VMotion Compatibility on a cluster, or change the EVC configuration on an EVC-enabled cluster, has failed because the selected EVC mode is not legal for the CPU hardware vendor of the hosts currently in the cluster.  ***Since:*** VI API 2.5u2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_cpu_vendor** | **str** | The CPU vendor in use in the cluster.  ***Since:*** VI API 2.5u2  | 
**mode_cpu_vendor** | **str** | The CPU vendor for the requested EVC mode.  ***Since:*** VI API 2.5u2  | 

## Example

```python
from vmware_vi.models.evc_mode_illegal_by_vendor import EVCModeIllegalByVendor

# TODO update the JSON string below
json = "{}"
# create an instance of EVCModeIllegalByVendor from a JSON string
evc_mode_illegal_by_vendor_instance = EVCModeIllegalByVendor.from_json(json)
# print the JSON string representation of the object
print EVCModeIllegalByVendor.to_json()

# convert the object into a dict
evc_mode_illegal_by_vendor_dict = evc_mode_illegal_by_vendor_instance.to_dict()
# create an instance of EVCModeIllegalByVendor from a dict
evc_mode_illegal_by_vendor_form_dict = evc_mode_illegal_by_vendor.from_dict(evc_mode_illegal_by_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


