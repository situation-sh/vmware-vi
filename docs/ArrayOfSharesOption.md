# ArrayOfSharesOption

A boxed array of *SharesOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SharesOption]**](SharesOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_shares_option import ArrayOfSharesOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSharesOption from a JSON string
array_of_shares_option_instance = ArrayOfSharesOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfSharesOption.to_json()

# convert the object into a dict
array_of_shares_option_dict = array_of_shares_option_instance.to_dict()
# create an instance of ArrayOfSharesOption from a dict
array_of_shares_option_form_dict = array_of_shares_option.from_dict(array_of_shares_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


