#!/usr/bin/env python
# coding: utf-8

# In[148]:


"""A video player class."""

import random

class VideoPlayer(VideoLibrary):
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.bool_stop = [True,True,True,True,True]
        self.bool_pause = [False,False,False,False,False]
        self.flag = [False,False,False,False,False]
        self.temp_playlist = []
        self.playlist_video = {}
        self.flag_reason = {}
        
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print('Here''s a list of all available videos:')
        for i in self._video_library._videos:
            title = self._video_library._videos[i].title
            tags = self._video_library._videos[i].tags
            id_vid = i
            if id_vid in list(self.flag_reason.keys()):  
                print(title+' ('+id_vid+')'+' ['+' '.join(tags)+'] '+' - FLAGGED (reason: '+ self.flag_reason[id_vid]+ ')')
            else:
                print(title+' ('+id_vid+')'+' ['+' '.join(tags)+']')
            
        print("show_all_videos needs implementation")

    def play_video(self, video_id): 
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """
        if video_id in list(self.flag_reason.keys()):
            print('Cannot play video: Video is currently flagged (reason: '+ self.flag_reason[video_id] +')')
        else:
            if video_id not in self._video_library._videos:
                print('Cannot play video: Video does not exist')
            else:
                for index, vid_id in enumerate(self._video_library._videos):
                    if self.bool_stop[index] == False:
                        print('Stopping video: ', self._video_library._videos[vid_id].title)
                        self.bool_stop[index] = True
                    if vid_id == video_id:
                        index_play, play = index, video_id
                print('Playing video: ',self._video_library._videos[video_id].title)
                self.bool_stop[index_play] = False
           
        print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        if all(self.bool_stop):
            print('Cannot stop video: No video is currently playing')
        else:
            for index, vid_id in enumerate(self._video_library._videos):
                if self.bool_stop[index] == False:
                    print('Stopping video: ', self._video_library._videos[vid_id].title)
                    self.bool_stop[index] = True
                    
        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        
        temp = list(self._video_library._videos.copy())
        for i in list(self.flag_reason.keys()):
            temp.remove(i)
            
        if temp != []:
            video_id = random.choice(temp)                        
            self.play_video(video_id)
        else:
            print('No videos available')

        
        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if all(self.bool_stop):
            print('Cannot pause video: No video is currently playing')
        else:
            for index, vid_id in enumerate(self._video_library._videos):
                if self.bool_stop[index] == False:
                    if self.bool_pause[index] == False:
                        print('Pausing video:', self._video_library._videos[vid_id].title)
                        self.bool_pause[index] = True
                    else:
                        print('Video already paused:', self._video_library._videos[vid_id].title)

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        
        if all(self.bool_stop):
            print('Cannot continue video: No video is currently playing')
        else:
            for index, vid_id in enumerate(self._video_library._videos):
                if self.bool_stop[index] == False:
                    if self.bool_pause[index] == False:
                        print('Cannot continue video: Video is not paused')
                    else:
                        print('Continuing video', self._video_library._videos[vid_id].title)
                        self.bool_pause[index] = False


        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if all(self.bool_stop):
            print('No video is currently playing')
        else:   
            for index, vid_id in enumerate(self._video_library._videos):
                if self.bool_stop[index] == False:
                    attr = self._video_library._videos[vid_id] 
                    title = attr.title
                    tags = attr.tags
                    if self.bool_pause[index] == False:
                        print('Currently playing:',title +' ('+vid_id+')'+' ['+' '.join(tags)+']')
                    else:
                        print('Currently playing:',title +' ('+vid_id+')'+' ['+' '.join(tags)+'] - '+ 'PAUSED')
                        
        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        temp = playlist_name.lower()
        if temp not in self.temp_playlist:
            print('Successfully created new playlist:', playlist_name)
            self.temp_playlist.append(temp)
            self.playlist_video[playlist_name] = []
        else:
            print('Cannot create playlist: A playlist with the same name already exists')
        
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        for index, vid_id in enumerate(self._video_library._videos):
            if vid_id == video_id:
                if self.flag[index] == True:
                    print('Cannot add video to my_playlist: Video is currently flagged (reason: '+ self.flag_reason[video_id])
        
        temp = playlist_name.lower()
        if video_id not in self._video_library._videos:
            print('Cannot add video to ', playlist_name, ': Video does not exist')
        elif temp not in self.temp_playlist:
            print('Cannot add video to ', playlist_name, ': Playlist does not exist')  
        else:
            if self._video_library._videos[video_id].title not in self.playlist_video[playlist_name]:
                self.playlist_video[playlist_name].append(self._video_library._videos[video_id].title)
                print('Added video to ',playlist_name, ':', self._video_library._videos[video_id].title)
            else:
                print('Cannot add video to ', playlist_name, ': Video already added')
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.temp_playlist) == 0:
            print('No playlists exist yet')
        else:
            print('Showing all my playlists')
            for i in self.playlist_video:
                print(i)
        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
        """
        temp = playlist_name.lower()
        if temp not in self.temp_playlist:
            print('Cannot show playlist', playlist_name, ': Playlist does not exist')
        else:
            print('Showing playlist: ',playlist_name)
            if (self.playlist_video[playlist_name] == []):
                print('\t No videos here yet')
            else:
                for title in self.playlist_video[playlist_name]:
                    for vid_id in self._video_library._videos:
                        if title == self._video_library._videos[vid_id].title:
                            attr = self._video_library._videos[vid_id]
                            titles = attr.title
                            tags = attr.tags  
                            if vid_id in list(self.flag_reason.keys()):  
                                print(title+' ('+vid_id+')'+' ['+' '.join(tags)+'] '+' - FLAGGED (reason: '+ self.flag_reason[vid_id]+ ')')
                            else:
                                print(title+' ('+vid_id+')'+' ['+' '.join(tags)+']')
         
        
        
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        temp = playlist_name.lower()
        if temp not in self.temp_playlist:
            print('Cannot remove video from '+playlist_name+': Playlist does not exist')
        else:
            if self._video_library._videos[video_id].title not in self.playlist_video[playlist_name]:
                print('Cannot remove video from '+playlist_name+ ': Video is not in playlist')
            else:
                self.playlist_video[playlist_name].remove(self._video_library._videos[video_id].title)
                print('Removed video from '+playlist_name+ ': '+ self._video_library._videos[video_id].title)
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        temp = playlist_name.lower()
        if playlist_name not in self.temp_playlist:
            print('Cannot clear playlist',playlist_name,': Playlist does not exist')
        else:
            self.playlist_video[playlist_name] = []
            print('Successfully removed all videos from ', playlist_name)
        
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in self.playlist_video:
            print('Cannot delete playlist my_playlist: Playlist does not exist')
        else:
            print('Deleted playlist', playlist_name)
            del self.playlist_video[playlist_name]

        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        temp = search_term.lower()
        temp_flag = self._video_library._videos.copy()
        for i in list(self.flag_reason.keys()):
            del temp_flag[i]
        list_search_vid = []
        for vid_id in temp_flag :
            if temp in temp_flag[vid_id].title.lower():
                attr = temp_flag[vid_id] 
                title = attr.title
                tags = attr.tags
                list_search_vid.append(title +' ('+vid_id+')'+' ['+' '.join(tags)+']')
            
             
        if list_search_vid != []:
            print('Here are the results for ',search_term)
            for i in range(len(list_search_vid)):
                print(str(i+1) + ') ' + list_search_vid[i])
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print('If your answer is not a valid number, we will assume it''s a no.')
            index_vid = eval(input())
            if index_vid not in range(1,len(list_search_vid)+1):
                pass
            else:
                print('Playing video:',list_search_vid[index_vid-1].split('(')[0])
        
                                    
            
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        
        temp_flag = self._video_library._videos.copy()
        for i in list(self.flag_reason.keys()):
            del temp_flag[i]
        tag = '#' + video_tag.lower()
        list_search_tag = []
        for vid_id in temp_flag:
            if tag in temp_flag[vid_id].tags:
                attr = temp_flag[vid_id] 
                title = attr.title
                tags = attr.tags
                list_search_tag.append(title +' ('+vid_id+')'+' ['+' '.join(tags)+']')
            
             
        if list_search_tag == []:
            print('No such results for ', video_tag)
        else:
            print('Here are the results for ',video_tag)
            for i in range(len(list_search_tag)):
                print(str(i+1) + ') ' + list_search_tag[i])
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print('If your answer is not a valid number, we will assume it''s a no.')
            index_vid = eval(input())
            if index_vid not in range(1,len(list_search_tag)+1):
                pass
            else:
                print('Playing video:',list_search_tag[index_vid-1].split('(')[0])
        
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason='Not supplied'):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        if video_id not in self._video_library._videos:
            print('Cannot flag video: Video does not exist')
        else: 
            for index, vid_id in enumerate(self._video_library._videos):
                if vid_id == video_id:
                    if self.flag[index] == False:
                        print('Successfully flagged video: '+ self._video_library._videos[vid_id].title + 
                              ' (reason: '+flag_reason )
                        self.flag_reason[vid_id] = flag_reason
                        self.flag[index] = True
                    else:
                        print('Cannot flag video: Video is already flagged')
        
        
        
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        if video_id not in self._video_library._videos:
            print('Cannot remove flag from video: Video does not exist')
        else: 
            for index, vid_id in enumerate(self._video_library._videos):
                if vid_id == video_id:
                    if self.flag[index] == True:
                        print('Successfully removed flag from video: '+ self._video_library._videos[vid_id].title)
                        self.flag[index] = False
                        del self.flag_reason[vid_id]
                    else:
                        print('Cannot remove flag from video: Video is not flag')
                        
        print("allow_video needs implementation")
        

