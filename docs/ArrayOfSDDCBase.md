# ArrayOfSDDCBase

A boxed array of *SDDCBase*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SDDCBase]**](SDDCBase.md) |  | 

## Example

```python
from vmware_vi.models.array_of_sddc_base import ArrayOfSDDCBase

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSDDCBase from a JSON string
array_of_sddc_base_instance = ArrayOfSDDCBase.from_json(json)
# print the JSON string representation of the object
print ArrayOfSDDCBase.to_json()

# convert the object into a dict
array_of_sddc_base_dict = array_of_sddc_base_instance.to_dict()
# create an instance of ArrayOfSDDCBase from a dict
array_of_sddc_base_form_dict = array_of_sddc_base.from_dict(array_of_sddc_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


