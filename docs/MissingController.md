# MissingController

A controller key has not been specified for a new device that requires a controller, such as a disk or CD-ROM device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.missing_controller import MissingController

# TODO update the JSON string below
json = "{}"
# create an instance of MissingController from a JSON string
missing_controller_instance = MissingController.from_json(json)
# print the JSON string representation of the object
print MissingController.to_json()

# convert the object into a dict
missing_controller_dict = missing_controller_instance.to_dict()
# create an instance of MissingController from a dict
missing_controller_form_dict = missing_controller.from_dict(missing_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


