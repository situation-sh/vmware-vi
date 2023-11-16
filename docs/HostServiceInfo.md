# HostServiceInfo

Data object describing the host service configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**List[HostService]**](HostService.md) | List of configured services.  | [optional] 

## Example

```python
from vmware_vi.models.host_service_info import HostServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostServiceInfo from a JSON string
host_service_info_instance = HostServiceInfo.from_json(json)
# print the JSON string representation of the object
print HostServiceInfo.to_json()

# convert the object into a dict
host_service_info_dict = host_service_info_instance.to_dict()
# create an instance of HostServiceInfo from a dict
host_service_info_form_dict = host_service_info.from_dict(host_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


