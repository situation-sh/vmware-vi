# InaccessibleVFlashSource

An InaccessibleVFlashSource exception is thrown when an attempt is made to access the vFlash resource on the host, such as creating vFlash cache file for the virtual disk.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Name of the host which has the vFlash resource  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.inaccessible_v_flash_source import InaccessibleVFlashSource

# TODO update the JSON string below
json = "{}"
# create an instance of InaccessibleVFlashSource from a JSON string
inaccessible_v_flash_source_instance = InaccessibleVFlashSource.from_json(json)
# print the JSON string representation of the object
print InaccessibleVFlashSource.to_json()

# convert the object into a dict
inaccessible_v_flash_source_dict = inaccessible_v_flash_source_instance.to_dict()
# create an instance of InaccessibleVFlashSource from a dict
inaccessible_v_flash_source_form_dict = inaccessible_v_flash_source.from_dict(inaccessible_v_flash_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


