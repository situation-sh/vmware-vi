# UnexpectedCustomizationFault

Error received when customization fails, possibly due to a scripting runtime error or invalid script parameters. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.unexpected_customization_fault import UnexpectedCustomizationFault

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpectedCustomizationFault from a JSON string
unexpected_customization_fault_instance = UnexpectedCustomizationFault.from_json(json)
# print the JSON string representation of the object
print UnexpectedCustomizationFault.to_json()

# convert the object into a dict
unexpected_customization_fault_dict = unexpected_customization_fault_instance.to_dict()
# create an instance of UnexpectedCustomizationFault from a dict
unexpected_customization_fault_form_dict = unexpected_customization_fault.from_dict(unexpected_customization_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


