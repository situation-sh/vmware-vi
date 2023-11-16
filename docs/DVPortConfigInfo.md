# DVPortConfigInfo

Management related configuration of a DistributedVirtualPort.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the port.  ***Since:*** vSphere API 4.0  | [optional] 
**scope** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Deprecated as of vSphere API 5.5.  The eligible entities that can connect to the port.  If unset, there is no restriction on which entity can connect to the port. If set, only the entities in the specified list or their child entities are allowed to connect to the port. If scopes are defined at both port and portgroup level, they are taken as an \&quot;AND\&quot; relationship. If such a relationship doesn&#39;t make sense, the reconfigure operation will raise an exception.  ***Since:*** vSphere API 4.0  Refers instances of *ManagedEntity*.  | [optional] 
**description** | **str** | A description string of the port.  ***Since:*** vSphere API 4.0  | [optional] 
**setting** | [**DVPortSetting**](DVPortSetting.md) |  | [optional] 
**config_version** | **str** | The version string of the configuration.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dv_port_config_info import DVPortConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortConfigInfo from a JSON string
dv_port_config_info_instance = DVPortConfigInfo.from_json(json)
# print the JSON string representation of the object
print DVPortConfigInfo.to_json()

# convert the object into a dict
dv_port_config_info_dict = dv_port_config_info_instance.to_dict()
# create an instance of DVPortConfigInfo from a dict
dv_port_config_info_form_dict = dv_port_config_info.from_dict(dv_port_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


