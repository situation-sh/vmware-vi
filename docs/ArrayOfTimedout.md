# ArrayOfTimedout

A boxed array of *Timedout*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Timedout]**](Timedout.md) |  | 

## Example

```python
from vmware_vi.models.array_of_timedout import ArrayOfTimedout

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTimedout from a JSON string
array_of_timedout_instance = ArrayOfTimedout.from_json(json)
# print the JSON string representation of the object
print ArrayOfTimedout.to_json()

# convert the object into a dict
array_of_timedout_dict = array_of_timedout_instance.to_dict()
# create an instance of ArrayOfTimedout from a dict
array_of_timedout_form_dict = array_of_timedout.from_dict(array_of_timedout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


