# ClusterComplianceCheckedEvent

This event records that a compliance check was triggered on the cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProfileEventArgument**](ProfileEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.cluster_compliance_checked_event import ClusterComplianceCheckedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComplianceCheckedEvent from a JSON string
cluster_compliance_checked_event_instance = ClusterComplianceCheckedEvent.from_json(json)
# print the JSON string representation of the object
print ClusterComplianceCheckedEvent.to_json()

# convert the object into a dict
cluster_compliance_checked_event_dict = cluster_compliance_checked_event_instance.to_dict()
# create an instance of ClusterComplianceCheckedEvent from a dict
cluster_compliance_checked_event_form_dict = cluster_compliance_checked_event.from_dict(cluster_compliance_checked_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


