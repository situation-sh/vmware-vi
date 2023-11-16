# Timedout

Timedout exception is thrown when a server abandons an operation that is taking longer than expected. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.timedout import Timedout

# TODO update the JSON string below
json = "{}"
# create an instance of Timedout from a JSON string
timedout_instance = Timedout.from_json(json)
# print the JSON string representation of the object
print Timedout.to_json()

# convert the object into a dict
timedout_dict = timedout_instance.to_dict()
# create an instance of Timedout from a dict
timedout_form_dict = timedout.from_dict(timedout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


