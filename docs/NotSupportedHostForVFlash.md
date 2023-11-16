# NotSupportedHostForVFlash

The host does not support vFlash feature.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.not_supported_host_for_v_flash import NotSupportedHostForVFlash

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedHostForVFlash from a JSON string
not_supported_host_for_v_flash_instance = NotSupportedHostForVFlash.from_json(json)
# print the JSON string representation of the object
print NotSupportedHostForVFlash.to_json()

# convert the object into a dict
not_supported_host_for_v_flash_dict = not_supported_host_for_v_flash_instance.to_dict()
# create an instance of NotSupportedHostForVFlash from a dict
not_supported_host_for_v_flash_form_dict = not_supported_host_for_v_flash.from_dict(not_supported_host_for_v_flash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


