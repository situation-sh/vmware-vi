# vmware_vi.AlarmManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alarm_manager_acknowledge_alarm**](AlarmManagerApi.md#alarm_manager_acknowledge_alarm) | **POST** /AlarmManager/{moId}/AcknowledgeAlarm | Acknowledge the alarm on a managed entity. 
[**alarm_manager_are_alarm_actions_enabled**](AlarmManagerApi.md#alarm_manager_are_alarm_actions_enabled) | **POST** /AlarmManager/{moId}/AreAlarmActionsEnabled | Returns true if alarm actions are enabled on the specified managed entity. 
[**alarm_manager_clear_triggered_alarms**](AlarmManagerApi.md#alarm_manager_clear_triggered_alarms) | **POST** /AlarmManager/{moId}/ClearTriggeredAlarms | Resets all triggered alarms to green. 
[**alarm_manager_create_alarm**](AlarmManagerApi.md#alarm_manager_create_alarm) | **POST** /AlarmManager/{moId}/CreateAlarm | Creates an alarm. 
[**alarm_manager_disable_alarm**](AlarmManagerApi.md#alarm_manager_disable_alarm) | **POST** /AlarmManager/{moId}/DisableAlarm | Disables alarm for a specific entity. 
[**alarm_manager_enable_alarm**](AlarmManagerApi.md#alarm_manager_enable_alarm) | **POST** /AlarmManager/{moId}/EnableAlarm | Enables alarm for a specific entity. 
[**alarm_manager_enable_alarm_actions**](AlarmManagerApi.md#alarm_manager_enable_alarm_actions) | **POST** /AlarmManager/{moId}/EnableAlarmActions | Enables or disables alarms on the specified managed entity. 
[**alarm_manager_get_alarm**](AlarmManagerApi.md#alarm_manager_get_alarm) | **POST** /AlarmManager/{moId}/GetAlarm | Available alarms defined on the entity. 
[**alarm_manager_get_alarm_state**](AlarmManagerApi.md#alarm_manager_get_alarm_state) | **POST** /AlarmManager/{moId}/GetAlarmState | The state of instantiated alarms on the entity. 
[**alarm_manager_get_default_expression**](AlarmManagerApi.md#alarm_manager_get_default_expression) | **GET** /AlarmManager/{moId}/defaultExpression | The default setting for each alarm expression, used to populate the initial client wizard screen. 
[**alarm_manager_get_description**](AlarmManagerApi.md#alarm_manager_get_description) | **GET** /AlarmManager/{moId}/description | The static descriptive strings used in alarms. 


# **alarm_manager_acknowledge_alarm**
> alarm_manager_acknowledge_alarm(mo_id, acknowledge_alarm_request_type)

Acknowledge the alarm on a managed entity. 

Acknowledge the alarm on a managed entity.  The actions associated with the alarm will not fire until the alarm's next distinct occurrence; that is, until after the alarm has entered the green or gray states at least once. Calling this method on an acknowledged or non-triggered alarm.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.acknowledge_alarm_request_type import AcknowledgeAlarmRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    acknowledge_alarm_request_type = vmware_vi.AcknowledgeAlarmRequestType() # AcknowledgeAlarmRequestType | 

    try:
        # Acknowledge the alarm on a managed entity. 
        api_instance.alarm_manager_acknowledge_alarm(mo_id, acknowledge_alarm_request_type)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_acknowledge_alarm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **acknowledge_alarm_request_type** | [**AcknowledgeAlarmRequestType**](AcknowledgeAlarmRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_are_alarm_actions_enabled**
> bool alarm_manager_are_alarm_actions_enabled(mo_id, are_alarm_actions_enabled_request_type)

Returns true if alarm actions are enabled on the specified managed entity. 

Returns true if alarm actions are enabled on the specified managed entity.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.are_alarm_actions_enabled_request_type import AreAlarmActionsEnabledRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    are_alarm_actions_enabled_request_type = vmware_vi.AreAlarmActionsEnabledRequestType() # AreAlarmActionsEnabledRequestType | 

    try:
        # Returns true if alarm actions are enabled on the specified managed entity. 
        api_response = api_instance.alarm_manager_are_alarm_actions_enabled(mo_id, are_alarm_actions_enabled_request_type)
        print("The response of AlarmManagerApi->alarm_manager_are_alarm_actions_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_are_alarm_actions_enabled: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **are_alarm_actions_enabled_request_type** | [**AreAlarmActionsEnabledRequestType**](AreAlarmActionsEnabledRequestType.md)|  | 

### Return type

**bool**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_clear_triggered_alarms**
> alarm_manager_clear_triggered_alarms(mo_id, clear_triggered_alarms_request_type)

Resets all triggered alarms to green. 

Resets all triggered alarms to green.  Should be used when mass alarm reset is needed.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Alarm.SetStatus 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.clear_triggered_alarms_request_type import ClearTriggeredAlarmsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    clear_triggered_alarms_request_type = vmware_vi.ClearTriggeredAlarmsRequestType() # ClearTriggeredAlarmsRequestType | 

    try:
        # Resets all triggered alarms to green. 
        api_instance.alarm_manager_clear_triggered_alarms(mo_id, clear_triggered_alarms_request_type)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_clear_triggered_alarms: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **clear_triggered_alarms_request_type** | [**ClearTriggeredAlarmsRequestType**](ClearTriggeredAlarmsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_create_alarm**
> ManagedObjectReference alarm_manager_create_alarm(mo_id, create_alarm_request_type)

Creates an alarm. 

Creates an alarm.  In addition to the Alarm.Create privilege, may also require the Global.ScriptAction if a RunScriptAction action is specified in the AlarmSpec. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_alarm_request_type import CreateAlarmRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_alarm_request_type = vmware_vi.CreateAlarmRequestType() # CreateAlarmRequestType | 

    try:
        # Creates an alarm. 
        api_response = api_instance.alarm_manager_create_alarm(mo_id, create_alarm_request_type)
        print("The response of AlarmManagerApi->alarm_manager_create_alarm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_create_alarm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_alarm_request_type** | [**CreateAlarmRequestType**](CreateAlarmRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A reference to the Alarm object created by the operation.  Refers instance of *Alarm*.  |  -  |
**500** | ***InvalidName***: if the alarm name is empty or too long.  ***DuplicateName***: if an alarm with the name already exists.  ***InvalidArgument***: if the specification is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_disable_alarm**
> alarm_manager_disable_alarm(mo_id, disable_alarm_request_type)

Disables alarm for a specific entity. 

Disables alarm for a specific entity.  ***Since:*** vSphere API 6.9.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disable_alarm_request_type import DisableAlarmRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    disable_alarm_request_type = vmware_vi.DisableAlarmRequestType() # DisableAlarmRequestType | 

    try:
        # Disables alarm for a specific entity. 
        api_instance.alarm_manager_disable_alarm(mo_id, disable_alarm_request_type)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_disable_alarm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **disable_alarm_request_type** | [**DisableAlarmRequestType**](DisableAlarmRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_enable_alarm**
> alarm_manager_enable_alarm(mo_id, enable_alarm_request_type)

Enables alarm for a specific entity. 

Enables alarm for a specific entity.  ***Since:*** vSphere API 6.9.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.enable_alarm_request_type import EnableAlarmRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    enable_alarm_request_type = vmware_vi.EnableAlarmRequestType() # EnableAlarmRequestType | 

    try:
        # Enables alarm for a specific entity. 
        api_instance.alarm_manager_enable_alarm(mo_id, enable_alarm_request_type)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_enable_alarm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **enable_alarm_request_type** | [**EnableAlarmRequestType**](EnableAlarmRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_enable_alarm_actions**
> alarm_manager_enable_alarm_actions(mo_id, enable_alarm_actions_request_type)

Enables or disables alarms on the specified managed entity. 

Enables or disables alarms on the specified managed entity.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.enable_alarm_actions_request_type import EnableAlarmActionsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    enable_alarm_actions_request_type = vmware_vi.EnableAlarmActionsRequestType() # EnableAlarmActionsRequestType | 

    try:
        # Enables or disables alarms on the specified managed entity. 
        api_instance.alarm_manager_enable_alarm_actions(mo_id, enable_alarm_actions_request_type)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_enable_alarm_actions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **enable_alarm_actions_request_type** | [**EnableAlarmActionsRequestType**](EnableAlarmActionsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_get_alarm**
> List[ManagedObjectReference] alarm_manager_get_alarm(mo_id, get_alarm_request_type)

Available alarms defined on the entity. 

Available alarms defined on the entity.  These alarms do not include any inherited alarms; that is, alarms associated with parent entities.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.get_alarm_request_type import GetAlarmRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    get_alarm_request_type = vmware_vi.GetAlarmRequestType() # GetAlarmRequestType | 

    try:
        # Available alarms defined on the entity. 
        api_response = api_instance.alarm_manager_get_alarm(mo_id, get_alarm_request_type)
        print("The response of AlarmManagerApi->alarm_manager_get_alarm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_get_alarm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **get_alarm_request_type** | [**GetAlarmRequestType**](GetAlarmRequestType.md)|  | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A reference to the Alarm objects returned by the operation.  Refers instances of *Alarm*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_get_alarm_state**
> List[AlarmState] alarm_manager_get_alarm_state(mo_id, get_alarm_state_request_type)

The state of instantiated alarms on the entity. 

The state of instantiated alarms on the entity. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.alarm_state import AlarmState
from vmware_vi.models.get_alarm_state_request_type import GetAlarmStateRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    get_alarm_state_request_type = vmware_vi.GetAlarmStateRequestType() # GetAlarmStateRequestType | 

    try:
        # The state of instantiated alarms on the entity. 
        api_response = api_instance.alarm_manager_get_alarm_state(mo_id, get_alarm_state_request_type)
        print("The response of AlarmManagerApi->alarm_manager_get_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_get_alarm_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **get_alarm_state_request_type** | [**GetAlarmStateRequestType**](GetAlarmStateRequestType.md)|  | 

### Return type

[**List[AlarmState]**](AlarmState.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of instantiated alarms.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_get_default_expression**
> List[AlarmExpression] alarm_manager_get_default_expression(mo_id)

The default setting for each alarm expression, used to populate the initial client wizard screen. 

The default setting for each alarm expression, used to populate the initial client wizard screen.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.alarm_expression import AlarmExpression
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The default setting for each alarm expression, used to populate the initial client wizard screen. 
        api_response = api_instance.alarm_manager_get_default_expression(mo_id)
        print("The response of AlarmManagerApi->alarm_manager_get_default_expression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_get_default_expression: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[AlarmExpression]**](AlarmExpression.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alarm_manager_get_description**
> AlarmDescription alarm_manager_get_description(mo_id)

The static descriptive strings used in alarms. 

The static descriptive strings used in alarms.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.alarm_description import AlarmDescription
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.AlarmManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The static descriptive strings used in alarms. 
        api_response = api_instance.alarm_manager_get_description(mo_id)
        print("The response of AlarmManagerApi->alarm_manager_get_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmManagerApi->alarm_manager_get_description: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**AlarmDescription**](AlarmDescription.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

