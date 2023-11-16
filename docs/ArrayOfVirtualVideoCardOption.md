# ArrayOfVirtualVideoCardOption

A boxed array of *VirtualVideoCardOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualVideoCardOption]**](VirtualVideoCardOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_video_card_option import ArrayOfVirtualVideoCardOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualVideoCardOption from a JSON string
array_of_virtual_video_card_option_instance = ArrayOfVirtualVideoCardOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualVideoCardOption.to_json()

# convert the object into a dict
array_of_virtual_video_card_option_dict = array_of_virtual_video_card_option_instance.to_dict()
# create an instance of ArrayOfVirtualVideoCardOption from a dict
array_of_virtual_video_card_option_form_dict = array_of_virtual_video_card_option.from_dict(array_of_virtual_video_card_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


