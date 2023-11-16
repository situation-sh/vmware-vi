# ArrayOfDVSSummary

A boxed array of *DVSSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSSummary]**](DVSSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_summary import ArrayOfDVSSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSSummary from a JSON string
array_of_dvs_summary_instance = ArrayOfDVSSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSSummary.to_json()

# convert the object into a dict
array_of_dvs_summary_dict = array_of_dvs_summary_instance.to_dict()
# create an instance of ArrayOfDVSSummary from a dict
array_of_dvs_summary_form_dict = array_of_dvs_summary.from_dict(array_of_dvs_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


