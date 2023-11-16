# ArrayOfDVSHealthCheckCapability

A boxed array of *DVSHealthCheckCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSHealthCheckCapability]**](DVSHealthCheckCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_health_check_capability import ArrayOfDVSHealthCheckCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSHealthCheckCapability from a JSON string
array_of_dvs_health_check_capability_instance = ArrayOfDVSHealthCheckCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSHealthCheckCapability.to_json()

# convert the object into a dict
array_of_dvs_health_check_capability_dict = array_of_dvs_health_check_capability_instance.to_dict()
# create an instance of ArrayOfDVSHealthCheckCapability from a dict
array_of_dvs_health_check_capability_form_dict = array_of_dvs_health_check_capability.from_dict(array_of_dvs_health_check_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


