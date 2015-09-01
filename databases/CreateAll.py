#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import engine, Base
import UsersCache

Base.metadata.create_all(engine)