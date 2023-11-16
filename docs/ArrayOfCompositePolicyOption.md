# ArrayOfCompositePolicyOption

A boxed array of *CompositePolicyOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CompositePolicyOption]**](CompositePolicyOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_composite_policy_option import ArrayOfCompositePolicyOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCompositePolicyOption from a JSON string
array_of_composite_policy_option_instance = ArrayOfCompositePolicyOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfCompositePolicyOption.to_json()

# convert the object into a dict
array_of_composite_policy_option_dict = array_of_composite_policy_option_instance.to_dict()
# create an instance of ArrayOfCompositePolicyOption from a dict
array_of_composite_policy_option_form_dict = array_of_composite_policy_option.from_dict(array_of_composite_policy_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


