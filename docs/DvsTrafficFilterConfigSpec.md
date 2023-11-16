# DvsTrafficFilterConfigSpec

The specification to reconfigure Traffic Filter.  This specification allows the user to do fine-grained updates for the Traffic Filter in the port settings. If the operation is *remove*, only the *DistributedVirtualPort.key* needs to be specified. If other fields are specified, they will be ignored. We cannot remove an inherited element. Only when the inherited flag is set to false and parent does not have an element with same key this operation succeeds. If the operation is *add*, then *DistributedVirtualPort.key* should not be specified and other fields need to be specified. The inherited flag should be set to false. If the operation is *edit*, then *DistributedVirtualPort.key* needs be specified and specify the other properties that need modification. If the inherited flag is set to true, a *DvsTrafficFilterConfig* object of same key must exist at the parent's level. The property values in the spec object will be ignored and use the values from the parent's *DvsTrafficFilterConfig* object instead. If inherited flag is set to false, then the new modifications will be applied.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Operation type.  See *ConfigSpecOperation_enum* for valid values.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.dvs_traffic_filter_config_spec import DvsTrafficFilterConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DvsTrafficFilterConfigSpec from a JSON string
dvs_traffic_filter_config_spec_instance = DvsTrafficFilterConfigSpec.from_json(json)
# print the JSON string representation of the object
print DvsTrafficFilterConfigSpec.to_json()

# convert the object into a dict
dvs_traffic_filter_config_spec_dict = dvs_traffic_filter_config_spec_instance.to_dict()
# create an instance of DvsTrafficFilterConfigSpec from a dict
dvs_traffic_filter_config_spec_form_dict = dvs_traffic_filter_config_spec.from_dict(dvs_traffic_filter_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


