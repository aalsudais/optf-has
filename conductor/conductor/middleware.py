#
# -------------------------------------------------------------------------
#   Copyright (c) 2015-2017 AT&T Intellectual Property
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# -------------------------------------------------------------------------
#

""" Middleware """

# from oslo_config import cfg
# import oslo_messaging
#
# from conductor.agent import plugin_base
# from conductor import sample
#
# OPTS = [
#     cfg.MultiStrOpt('http_control_exchanges',
#                     default=[cfg.CONF.nova_control_exchange,
#                              cfg.CONF.glance_control_exchange,
#                              cfg.CONF.neutron_control_exchange,
#                              cfg.CONF.cinder_control_exchange],
#                     help="Exchanges name to listen for notifications."),
# ]
#
# cfg.CONF.register_opts(OPTS)
#
#
# class HTTPRequest(plugin_base.NotificationBase,
#                   plugin_base.NonMetricNotificationBase):
#     event_types = ['http.request']
#
#     def get_targets(self, conf):
#         """Return a sequence of oslo_messaging.Target
#         This sequence is defining the exchange and topics to be connected for
#         this plugin.
#         """
#         return [oslo_messaging.Target(topic=topic, exchange=exchange)
#                 for topic in self.get_notification_topics(conf)
#                 for exchange in conf.http_control_exchanges]
#
#     def process_notification(self, message):
#         yield sample.Sample.from_notification(
#             name=message['event_type'],
#             type=sample.TYPE_DELTA,
#             volume=1,
#             unit=message['event_type'].split('.')[1],
#             user_id=message['payload']['request'].get('HTTP_X_USER_ID'),
#             project_id=message['payload']['request'].get('HTTP_X_PROJECT_ID'),
#             resource_id=message['payload']['request'].get(
#                 'HTTP_X_SERVICE_NAME'),
#             message=message)
#
#
# class HTTPResponse(HTTPRequest):
#     event_types = ['http.response']
