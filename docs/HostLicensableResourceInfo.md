# HostLicensableResourceInfo

Encapsulates information about all licensable resources on the host.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**List[KeyAnyValue]**](KeyAnyValue.md) | List of currently supported resources.  The type of every value is long. The key can be one of *HostLicensableResourceKey_enum* or arbitrary string.  NOTE: The values in this property may not be accurate for pre-5.0 hosts when returned by vCenter 5.0  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_licensable_resource_info import HostLicensableResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostLicensableResourceInfo from a JSON string
host_licensable_resource_info_instance = HostLicensableResourceInfo.from_json(json)
# print the JSON string representation of the object
print HostLicensableResourceInfo.to_json()

# convert the object into a dict
host_licensable_resource_info_dict = host_licensable_resource_info_instance.to_dict()
# create an instance of HostLicensableResourceInfo from a dict
host_licensable_resource_info_form_dict = host_licensable_resource_info.from_dict(host_licensable_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


