# NonVIWorkloadDetectedOnDatastoreEvent

This event records that non-VI workload is detected on the datastore.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.non_vi_workload_detected_on_datastore_event import NonVIWorkloadDetectedOnDatastoreEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NonVIWorkloadDetectedOnDatastoreEvent from a JSON string
non_vi_workload_detected_on_datastore_event_instance = NonVIWorkloadDetectedOnDatastoreEvent.from_json(json)
# print the JSON string representation of the object
print NonVIWorkloadDetectedOnDatastoreEvent.to_json()

# convert the object into a dict
non_vi_workload_detected_on_datastore_event_dict = non_vi_workload_detected_on_datastore_event_instance.to_dict()
# create an instance of NonVIWorkloadDetectedOnDatastoreEvent from a dict
non_vi_workload_detected_on_datastore_event_form_dict = non_vi_workload_detected_on_datastore_event.from_dict(non_vi_workload_detected_on_datastore_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


