package data

import (
	"errors"
	"fmt"
)

type Friend struct {
	name string
}

func NewFriend(name string) *Friend {
	return &Friend{
		name: name,
	}
}

func (f *Friend) Name() string {
	return f.name
}

type FriendsDb interface {
	Add(*Friend) error
	List() []*Friend
}

type MemoryFriendsDb struct {
	friends map[string]*Friend
}

func NewMemoryFriendsDb() MemoryFriendsDb {
	return MemoryFriendsDb{
		friends: make(map[string]*Friend),
	}
}

func (mfdb MemoryFriendsDb) Add(f *Friend) error {
	if _, ok := mfdb.friends[f.name]; ok {
		return errors.New(fmt.Sprintf("%s is already in friends list.", f.name))
	}
	mfdb.friends[f.name] = f
	return nil
}

func (mfdb MemoryFriendsDb) List() []*Friend {
	list := make([]*Friend, 0)
	for _, f := range mfdb.friends {
		list = append(list, f)
	}
	return list
}
