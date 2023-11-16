# DVPortConfigSpec

Specification to reconfigure a *DistributedVirtualPort*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation to remove or modify the existing ports.  The valid values are: - *edit* - *remove*    ***Since:*** vSphere API 4.0  | 
**key** | **str** | Key of the port to be reconfigured.  ***Since:*** vSphere API 4.0  | [optional] 
**name** | **str** | The name of the port.  ***Since:*** vSphere API 4.0  | [optional] 
**scope** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Deprecated as of vSphere API 5.5.  The eligible entities that can connect to the port, for detail see *DVPortConfigInfo.scope*.  ***Since:*** vSphere API 4.0  Refers instances of *ManagedEntity*.  | [optional] 
**description** | **str** | The description string of the port.  ***Since:*** vSphere API 4.0  | [optional] 
**setting** | [**DVPortSetting**](DVPortSetting.md) |  | [optional] 
**config_version** | **str** | The version string of the configuration.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.dv_port_config_spec import DVPortConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortConfigSpec from a JSON string
dv_port_config_spec_instance = DVPortConfigSpec.from_json(json)
# print the JSON string representation of the object
print DVPortConfigSpec.to_json()

# convert the object into a dict
dv_port_config_spec_dict = dv_port_config_spec_instance.to_dict()
# create an instance of DVPortConfigSpec from a dict
dv_port_config_spec_form_dict = dv_port_config_spec.from_dict(dv_port_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


