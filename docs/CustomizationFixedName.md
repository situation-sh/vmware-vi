# CustomizationFixedName

A fixed name. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The virtual machine name specified by the client.  | 

## Example

```python
from vmware_vi.models.customization_fixed_name import CustomizationFixedName

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationFixedName from a JSON string
customization_fixed_name_instance = CustomizationFixedName.from_json(json)
# print the JSON string representation of the object
print CustomizationFixedName.to_json()

# convert the object into a dict
customization_fixed_name_dict = customization_fixed_name_instance.to_dict()
# create an instance of CustomizationFixedName from a dict
customization_fixed_name_form_dict = customization_fixed_name.from_dict(customization_fixed_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


