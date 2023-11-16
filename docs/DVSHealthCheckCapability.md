# DVSHealthCheckCapability

Health check capabilities of health check supported by the vSphere Distributed Switch  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_health_check_capability import DVSHealthCheckCapability

# TODO update the JSON string below
json = "{}"
# create an instance of DVSHealthCheckCapability from a JSON string
dvs_health_check_capability_instance = DVSHealthCheckCapability.from_json(json)
# print the JSON string representation of the object
print DVSHealthCheckCapability.to_json()

# convert the object into a dict
dvs_health_check_capability_dict = dvs_health_check_capability_instance.to_dict()
# create an instance of DVSHealthCheckCapability from a dict
dvs_health_check_capability_form_dict = dvs_health_check_capability.from_dict(dvs_health_check_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


