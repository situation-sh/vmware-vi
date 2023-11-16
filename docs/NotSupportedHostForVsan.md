# NotSupportedHostForVsan

The host does not support VSAN.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.not_supported_host_for_vsan import NotSupportedHostForVsan

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedHostForVsan from a JSON string
not_supported_host_for_vsan_instance = NotSupportedHostForVsan.from_json(json)
# print the JSON string representation of the object
print NotSupportedHostForVsan.to_json()

# convert the object into a dict
not_supported_host_for_vsan_dict = not_supported_host_for_vsan_instance.to_dict()
# create an instance of NotSupportedHostForVsan from a dict
not_supported_host_for_vsan_form_dict = not_supported_host_for_vsan.from_dict(not_supported_host_for_vsan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


