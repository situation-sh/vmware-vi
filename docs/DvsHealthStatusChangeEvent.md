# DvsHealthStatusChangeEvent

Health check status of an switch is changed.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_uuid** | **str** | UUID of the DVS the host is connected to.  ***Since:*** vSphere API 5.1  | 
**health_result** | [**HostMemberHealthCheckResult**](HostMemberHealthCheckResult.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_health_status_change_event import DvsHealthStatusChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsHealthStatusChangeEvent from a JSON string
dvs_health_status_change_event_instance = DvsHealthStatusChangeEvent.from_json(json)
# print the JSON string representation of the object
print DvsHealthStatusChangeEvent.to_json()

# convert the object into a dict
dvs_health_status_change_event_dict = dvs_health_status_change_event_instance.to_dict()
# create an instance of DvsHealthStatusChangeEvent from a dict
dvs_health_status_change_event_form_dict = dvs_health_status_change_event.from_dict(dvs_health_status_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


