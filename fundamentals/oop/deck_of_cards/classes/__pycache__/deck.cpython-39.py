a
    ��`�  �                   @   s   d dl mZ G dd� d�ZdS )�   )�cardc                   @   s   e Zd Zdd� Zdd� ZdS )�Deckc              	   C   s�   g d�}g | _ |D ]n}tdd�D ]^}d}|dkr6d}n2|dkrDd}n$|dkrRd	}n|d
kr`d}nt|�}| j �t�|||�� q qd S )N)ZspadesZheartsZclubsZdiamondsr   �   � ZAce�   ZJack�   ZQueen�   ZKing)�cards�range�str�appendr   ZCard)�selfZsuits�s�iZstr_val� r   �Q/Users/adrienjdion/Desktop/python_admin/hack_a_thon/deck_of_cards/classes/deck.py�__init__   s    zDeck.__init__c                 C   s   | j D ]}|��  qd S )N)r	   Z	card_info)r   r   r   r   r   �
show_cards   s    
zDeck.show_cardsN)�__name__�
__module__�__qualname__r   r   r   r   r   r   r      s   r   N)r   r   r   r   r   r   r   �<module>   s   