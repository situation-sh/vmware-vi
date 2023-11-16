# InvalidController

An InvalidController exception is thrown if a device refers to a controller that cannot be found.  For example, an exception might be thrown if the client incorrectly passes a controller key, or if the client did not specify a controller where one is required (such as for disks or CD-ROMs). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_key** | **int** |  | 

## Example

```python
from vmware_vi.models.invalid_controller import InvalidController

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidController from a JSON string
invalid_controller_instance = InvalidController.from_json(json)
# print the JSON string representation of the object
print InvalidController.to_json()

# convert the object into a dict
invalid_controller_dict = invalid_controller_instance.to_dict()
# create an instance of InvalidController from a dict
invalid_controller_form_dict = invalid_controller.from_dict(invalid_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


