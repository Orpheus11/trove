# Copyright 2015 Tesora Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from trove.common.db.cassandra import models as guest_models
from trove.extensions.common.service import DefaultRootController
from trove.extensions.mysql import models


class CassandraRootController(DefaultRootController):

    def _find_root_user(self, context, instance_id):
        user = guest_models.CassandraUser.root()
        # TODO(pmalik): Using MySQL model until we have datastore specific
        # extensions (bug/1498573).
        return models.User.load(
            context, instance_id, user.name, user.host, root_user=True)
