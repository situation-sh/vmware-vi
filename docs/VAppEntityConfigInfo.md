# VAppEntityConfigInfo

This object type describes the behavior of an entity (virtual machine or sub-vApp container) in a vApp container.  The auto-start/auto-stop configurations control the behavior of the start/stop vApp operations.  An virtual machine entity can be configured to wait for a period of time before starting or to wait to receive a successful heartbeat from a virtual machine before starting the next virtual machine in the sequence. - For a power-on operation, if waitForHeartbeat is true, then the power-on   sequence continues after the the first heartbeat has been received. If   waitingForGuest is false, the system waits for the specified delay and   then continues the power-on sequence. - For a power-off operation, if delay is non-zero, the requested power-off   action is invoked (powerOff, suspend, guestShutdown) on the virtual   machine and the system waits until the number of seconds specified in the   delay have passed.    If startAction and stopAction for an entity are both set to none, that entity does not participate in the sequence.  The start/stop delay and waitingForGuest is not used if the entity is a vApp container. For a vApp the only value values for startAction is none or powerOn, and the valid values for stopAction is none or powerOff.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**tag** | **str** | Tag for entity.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**start_order** | **int** | Specifies the start order for this entity.  Entities are started from lower numbers to higher-numbers and reverse on shutdown. Multiple entities with the same start-order can be started in parallel and the order is unspecified. This value must be 0 or higher.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**start_delay** | **int** | Delay in seconds before continuing with the next entity in the order of entities to be started.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**waiting_for_guest** | **bool** | Determines if the virtual machine should start after receiving a heartbeat, from the guest.  When a virtual machine is next in the start order, the system either waits a specified period of time for a virtual machine to power on or it waits until it receives a successful heartbeat from a powered on virtual machine. By default, this is set to false.  This property has no effect for vApps.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**start_action** | **str** | How to start the entity.  Valid settings are none or powerOn. If set to none, then the entity does not participate in auto-start.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**stop_delay** | **int** | Delay in seconds before continuing with the next entity in the order sequence.  This is only used if the stopAction is guestShutdown.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**stop_action** | **str** | Defines the stop action for the entity.  Can be set to none, powerOff, guestShutdown, or suspend. If set to none, then the entity does not participate in auto-stop.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**destroy_with_parent** | **bool** | Deprecated as of vSphere API 5.1.  Whether the entity should be removed, when this vApp is removed.  This is only set for linked children.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.v_app_entity_config_info import VAppEntityConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VAppEntityConfigInfo from a JSON string
v_app_entity_config_info_instance = VAppEntityConfigInfo.from_json(json)
# print the JSON string representation of the object
print VAppEntityConfigInfo.to_json()

# convert the object into a dict
v_app_entity_config_info_dict = v_app_entity_config_info_instance.to_dict()
# create an instance of VAppEntityConfigInfo from a dict
v_app_entity_config_info_form_dict = v_app_entity_config_info.from_dict(v_app_entity_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


