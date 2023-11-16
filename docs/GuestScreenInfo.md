# GuestScreenInfo

Screen settings 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | Width of the screen in pixels.  | 
**height** | **int** | Height of the screen in pixels.  | 

## Example

```python
from vmware_vi.models.guest_screen_info import GuestScreenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestScreenInfo from a JSON string
guest_screen_info_instance = GuestScreenInfo.from_json(json)
# print the JSON string representation of the object
print GuestScreenInfo.to_json()

# convert the object into a dict
guest_screen_info_dict = guest_screen_info_instance.to_dict()
# create an instance of GuestScreenInfo from a dict
guest_screen_info_form_dict = guest_screen_info.from_dict(guest_screen_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


